import React, { Component } from 'react';
import axios from 'axios';
import DisplayVideo from './DisplayVideo';
import SearchBar from './SearchBar';
import VideoCollection from './VideoCollection';

class App extends Component {

    constructor(props) {
        super(props);
        this.state = { 
            videoId: '',
            videos: []
         }
    }

    componentDidMount(){
        this.getVideos('true crime');
    }

    getVideos = async (searchTerm) => {
        let response = await axios.get(`https://www.googleapis.com/youtube/v3/search?q=${searchTerm}&type=video&key=AIzaSyC_0I7RZto-QzJCISRnYOJOM938SvMPmnU&part=snippet`)
        console.log('videos', response.data.items)
        this.setState({
          videoId: response.data.items[0].id.videoId,
          videos: response.data.items
        });
    }


    render() { 
        return ( 
            <div>
                <h1>YouTube Clone</h1>
                <DisplayVideo videoId={this.state.videoId} />
                <SearchBar search={this.getVideos}/>
                <VideoCollection videos={this.state.videos}/>
            </div>
         );
    }
}
 
export default App;