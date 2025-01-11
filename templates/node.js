const express = require('express');
const bodyParser = require('body-parser');
const nodemailer = require('nodemailer');
const app = express();

app.use(bodyParser.json());

app.post('/signup', (req, res) => {
    const { email, password } = req.body;
    // Save user details to a database (e.g., MongoDB, MySQL)

    // Send a confirmation email to the user
    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'your-email@gmail.com',
            pass: 'your-email-password'
        }
    });

    const mailOptions = {
        from: 'your-email@gmail.com',
        to: email,
        subject: 'Signup Confirmation',
        text: 'Thank you for signing up!'
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            return console.log(error);
        }
        console.log('Email sent: ' + info.response);
    });

    res.json({ message: 'User signed up and email sent!' });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
