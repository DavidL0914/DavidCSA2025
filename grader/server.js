// server.js
require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());
app.use(express.static('public'));

// Endpoint to handle grading
app.post('/grade', async (req, res) => {
    const { prompt, code } = req.body;

    // Construct the prompt for ChatGPT
    const gptPrompt = `Grade the following code submission based on the prompt: "${prompt}". The code is: "${code}". Provide a grade from 0 to 1, and give feedback on why they received that grade.`;

    try {
        const response = await axios.post('https://api.openai.com/v1/chat/completions', {
            model: 'gpt-3.5-turbo',
            messages: [{ role: 'user', content: gptPrompt }],
        }, {
            headers: {
                'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,
                'Content-Type': 'application/json',
            },
        });

        const result = response.data.choices[0].message.content;
        res.json({ result });
    } catch (error) {
        console.error('Error calling OpenAI API:', error);
        res.status(500).send('Error grading code submission');
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
