const express = require('express');
const multer = require('multer');
const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');

const app = express();
const port = 3000;
const upload = multer();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Root route to verify the server is running
app.get('/', (req, res) => {
    res.send('Welcome to the Speech Processing API');
});

app.post('/api/speech', upload.single('audio'), (req, res) => {
    if (!req.file) {
        return res.status(400).send('No file uploaded.');
    }

    // Define the path for the audio file
    const audioFilePath = path.join(__dirname, 'audio.wav');
    fs.writeFileSync(audioFilePath, req.file.buffer);

    exec(`python process_audio.py ${audioFilePath}`, (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            return res.status(500).send('Error processing audio');
        }
        res.json({ result: stdout });
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
