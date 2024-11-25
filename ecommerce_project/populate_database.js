const { exec } = require('child_process');
const util = require('util');

const execPromise = util.promisify(exec);

async function runCommand(command) {
    try {
        const { stdout, stderr } = await execPromise(command);
        console.log('stdout:', stdout);
        if (stderr) console.error('stderr:', stderr);
    } catch (error) {
        console.error('Error:', error);
    }
}

async function populateDatabase() {
    console.log('Creating placeholder images...');
    await runCommand('python create_placeholder_images.py');

    console.log('Running migrations...');
    await runCommand('python manage.py makemigrations');
    await runCommand('python manage.py migrate');

    console.log('Populating database with products and categories...');
    await runCommand('python manage.py populate_products');

    console.log('Database population complete!');
}

populateDatabase();

