
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

/**
 * Maintain a simple map of React components to make it easier
 * for Django to reference individual components
 */
const pages = {
  App,
}

/**
 * If Django hasn't injected these properties into the HTML
 * template that's loading this script then we're viewing it
 * via the create-react-app liveserver
 */
window.component = window.component || 'App';
window.reactRoot = window.reactRoot || document.getElementById('react');
window.props = window.props || { };

// Check if production for websocket
const is_production = ('is_production' in window.props) ? !!window.props.is_production : false;

// To acces the component for inserting new contentState
// Source 1: https://stackoverflow.com/questions/31612598/call-a-react-component-method-from-outside
// Source 2: https://stackoverflow.com/questions/24841855/how-to-access-component-methods-from-outside-in-reactjs
// Source 3: https://reactjs.org/docs/refs-and-the-dom.html#adding-a-ref-to-a-class-component
window.props.ref = (element) => {
  window.reactComponent = element
}

ReactDOM.render(
    <App is_production={is_production} />,
    document.getElementById('react')
);
