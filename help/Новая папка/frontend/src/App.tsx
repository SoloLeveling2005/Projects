import React from 'react';
import './App.css';
import { getSites } from './actions/site/action';
import { connect } from "react-redux";

interface AppProps {
  getSites: () => void
}

const App: React.FC<AppProps> = ({ getSites }) => {
    
// в App ничего не пиши;
// Все основные компоненты на одном уровне как App будут находится в папке pages

React.useEffect(() => {
  getSites()
}, [])

return (
    <div className="App">

    </div>
  );
}

export default connect(null, { getSites })(App);
