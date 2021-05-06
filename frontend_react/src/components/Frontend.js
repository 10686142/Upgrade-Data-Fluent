import React, {Component} from 'react';
import PropTypes from 'prop-types';

class Frontend extends Component {
    constructor(props) {
        super(props);
        console.log("Frontend loaded....");
    }

    render() {
        return (<div>
            `TODO: Add implementation and production: ${this.props.is_production.toString()}`
        </div>);
    }

}
Frontend.propTypes = {
    is_production: PropTypes.bool.isRequired
}
export default Frontend;
