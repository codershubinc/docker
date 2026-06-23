import express from 'express';

const app = express();
const PORT = 3000;

// Middleware to parse JSON bodies, which is needed for POST requests
app.use(express.json());

// In-memory data store for demonstration purposes
const users = [
    { id: 1, name: 'Alice', email: 'alice@example.com' },
    { id: 2, name: 'Bob', email: 'bob@example.com' },
    { id: 3, name: 'Charlie', email: 'charlie@example.com' },
    { id: 4, name: 'Diana', email: 'diana@example.com' }
];

app.get('/', (req, res) => {
    res.send('Hello World!');
});

// GET all users
app.get('/api/users', (req, res) => {
    res.json(users);
});

// GET a single user by id
app.get('/api/users/:id', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    if (!user) return res.status(404).send('User not found.');
    res.json(user);
});

// POST (create) a new user
app.post('/api/users', (req, res) => {
    const { name, email } = req.body;
    if (!name) {
        return res.status(400).send('Name is required.');
    }

    // A simple (optional) check for email format
    if (email && !/^\S+@\S+\.\S+$/.test(email)) {
        return res.status(400).send('Invalid email format.');
    }

    const newUser = {
        id: users.length > 0 ? Math.max(...users.map(u => u.id)) + 1 : 1,
        name: name,
        email: email
    };
    users.push(newUser);
    res.status(201).json(newUser);
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
