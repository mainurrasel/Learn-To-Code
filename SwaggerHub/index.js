'use strict';

const Hapi = require('hapi');
const fs = require('fs');
const util = require('util');

const readFile = util.promisify(fs.readFile);
const writeFile = util.promisify(fs.writeFile);

const init = async () => {

    const server = Hapi.server({
        port: 3000,
        host: 'localhost'
    });

    server.route({
        method: 'GET',
        path: '/',
        handler: (request, h) => {
            return 'Hello World!';
        }
    });

    server.route({
        method: 'GET',
        path: '/book-list',
        options: {
            handler: async (request, h) => {
                const books = await readFile('./books.json', 'utf8');
                return h.response(JSON.parse(books));
            }
        }
    });
    
    server.route({
        method: 'POST',
        path: '/add-book',
        options: {
            handler: async (request, h) => {
                const book = JSON.parse(request.payload);
                let books = await readFile('./books.json', 'utf8');
                books = JSON.parse(books);
                book.id = books.length + 1;
                books.push(book);
                await writeFile('./books.json', JSON.stringify(books, null, 2), 'utf8');
                return h.response(books).code(200);
            }
        }
    });
    
    server.route({
        method: 'PUT',
        path: '/update-book-list/{id}',
        options: {
            handler: async (request, h) => {
                const updBook = JSON.parse(request.payload);
                const id = request.params.id;
                let books = await readFile('./books.json', 'utf8');
                books = JSON.parse(books);
                books.forEach((book) => {
                    if (book.id == id) {
                        book.title = updBook.title;
                        book.author = updBook.author;
                    }
                });
                await writeFile('./books.json', JSON.stringify(books, null, 2), 'utf8');
                return h.response(books).code(200);
            }
        }
    });
    
    server.route({
        method: 'DELETE',
        path: '/delete-book/{id}',
        options: {
            handler: async (request, h) => {
                const updBook = JSON.parse(request.payload);
                const id = request.params.id;
                let books = await readFile('./books.json', 'utf8');
                books = JSON.parse(books);
                books = books.filter(book => book.id != id);
                await writeFile('./books.json', JSON.stringify(books, null, 2), 'utf8');
                return h.response(books).code(200);
            }
        }
    });

    await server.start();
    console.log('Server running on %s', server.info.uri);
};

process.on('unhandledRejection', (err) => {

    console.log(err);
    process.exit(1);
});

init();