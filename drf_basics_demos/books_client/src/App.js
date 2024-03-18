import logo from './logo.svg';
import './App.css';
import {useEffect, useState} from "react";

const Loader = () => {
    return <div>
        <img src={logo}/>
    </div>
};
const BooksList = () => {
    const [books, setBooks] = useState([]);

    useEffect(() => {
        fetch("http://localhost:8000/api/books/")
            .then(resp => resp.json())
            .then(books => setBooks(books));
    }, []);

    if (books.length === 0) {
        return <Loader/>
    }

    return (
        <ul>
            {books.map(book => (
                <li>
                    {book.title} by {book.author.name}
                </li>
            ))}
        </ul>
    )
};


const App = () => {
    return (
        <div className="App">
            <BooksList/>
        </div>
    );
};

export default App;
