import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header>
          {/*<img src="./img/ico.png" alt="" className='logo'/>*/}
        <div className="find">
            <input type="text" placeholder="What do you need"/>
            <button>Search</button>
        </div>
      </header>
        <section className='sites'>
            <div className="site">
                <a href="http://127.0.0.1:8001/" className="url">
                    https://www.Site1.com
                </a>
                <br/>
                <a href="http://127.0.0.1:8001/" className="title">
                    Site1
                </a>
                <br/>
                <p className="description">
                    TextTextTextTextTextTextTextTextTextTextTextText
                </p>
            </div>
            <div className="site">
                <a href="" className="url">
                    https://www.Site1.com
                </a>
                <br/>
                <a href="" className="title">
                    Site1
                </a>
                <br/>
                <p className="description">
                    TextTextTextTextTextTextTextTextTextTextTextText
                </p>
            </div>
            <div className="site">
                <a href="" className="url">
                    https://www.Site1.com
                </a>
                <br/>
                <a href="" className="title">
                    Site1
                </a>
                <br/>
                <p className="description">
                    TextTextTextTextTextTextTextTextTextTextTextText
                </p>
            </div>
        </section>
    </div>
  );
}

export default App;
