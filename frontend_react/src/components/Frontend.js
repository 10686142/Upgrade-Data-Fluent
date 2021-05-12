import React, {Component} from 'react';
import PropTypes from 'prop-types';

class Frontend extends Component {
    constructor(props) {
        super(props);
        console.log("Frontend loaded....");
        // User variable from django if applicable
        this.state = {
            listnersAdded: false,
            isSendingData: false,
            formText:"",
            webSocket: {},
        };
    }

    componentDidMount(){
        this.setupWebSocket();
    }

    setupWebSocket(){
        const domain = 'localhost';
        var socketPath = "wss://"+ domain + ":8000/";

        const webSocket = new WebSocket(socketPath);

        this.setState({ webSocket:webSocket });

        // Received downstream websocket message
        webSocket.onmessage = (e) => {
            var data = JSON.parse(e.data);
            console.log(data);
            alert(data);
        };

        webSocket.onclose = (e) => {
            console.error('Chat socket closed unexpectedly');
            console.error(e);
        };
    }

    async sendMessage(){
        // Clear previous data
        this.setState({
            isTracking: true,
            formText: ""
        });

        this.sendDataUpstream({ message:"Tracking starts.." }, false, true);
    }

    handleInputChange = (event) => {
      this.setState({ formText: event.target.term })
    }

    sendDataUpstream = (data) => {
        this.state.webSocket.send(JSON.stringify({
            'msg': 'This has been send upstream!',
            'data':data
        }));
    }

    render() {
        return(
          <div className="center">
            <h1>Fill our message to send upstream</h1>
            <form>
            <fieldset>
               <label>
                 <input name="name" onChange={this.handleInputChange}/>
               </label>
             </fieldset>
             <button type="submit" onClick={this.sendMessage}>Submit</button>
            </form>
          </div>
        )
    }

}
Frontend.propTypes = {
    is_production: PropTypes.bool.isRequired
}
export default Frontend;
