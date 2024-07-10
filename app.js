const express = require('express');
const path = require('path');
const { Pool } = require('pg');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 3000;

const pool = new Pool({
    connectionString: process.env.DATABASE_URL
});

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', async (req, res) => {
    const client = await pool.connect();
    try {
        const result = await client.query('SELECT * FROM emprendimiento');
        res.render('index', { emprendimientos: result.rows });
    } finally {
        client.release();
    }
});

app.get('/profile/:run', async (req, res) => {
    const { run } = req.params;
    const client = await pool.connect();
    try {
        const result = await client.query('SELECT * FROM emprendimiento WHERE run = $1', [run]);
        const emprendimiento = result.rows[0];

        // Asegúrate de que la consulta a la tabla "detalle" esté correcta
        const detalleResult = await client.query('SELECT * FROM detalle WHERE emprendimiento_id = $1', [emprendimiento.id]);
        const detalle = detalleResult.rows[0];

        // Pasa tanto "emprendimiento" como "detalle" a la plantilla
        res.render('profile', { emprendimiento, detalle });
    } finally {
        client.release();
    }
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
