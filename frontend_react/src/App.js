import React, {Component} from 'react';
import PropTypes from 'prop-types';
import Frontend from './components/Frontend'


// Button From: https://reactjsexample.com/simple-react-component-for-a-circular-progress-button/
// State in parent component & explantion 2 editor: https://stackoverflow.com/questions/43001280/accessing-draftjs-output-from-parent
class App extends Component {

  render() {
    return (
      <div className="react_app">
        <Frontend
        is_production={this.props.is_production}
        />
      </div>
    );
  }
}

App.propTypes = {
    is_production: PropTypes.bool.isRequired,
}

export default App;
