import React, { Component } from 'react';
import axios from 'axios';
import DisplayVideo from './components/DisplayVideo';
import SearchBar from './components/SearchBar';

class App extends Component {

    constructor(props) {
        super(props);
        this.state = { 
            videoId: ''
         }
    }

    componentDidMount(){
        this.getVideos('true crime');
    }

    getVideos = async (searchTerm) => {
        let response = await axios.get(`https://www.googleapis.com/youtube/v3/search?q=${searchTerm}&type=video&key=AIzaSyC_0I7RZto-QzJCISRnYOJOM938SvMPmnU&part=snippet`)
        console.log(response.data)
        this.setState({
          videoId: response.data.items[0].id.videoId
        });
    }


    render() { 
        return ( 
            <div>
                <h1>YouTube Clone</h1>
                <DisplayVideo videoId={this.state.videoId} />
                <SearchBar search={this.getVideos}/>

            </div>
         );
    }
}
 
export default App;