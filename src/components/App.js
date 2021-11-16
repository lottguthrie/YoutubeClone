import React from 'react';
import SearchBar from './SearchBar';
import DisplayVideo from './DisplayVideo';
import VideoCollection from './VideoCollection'
import axios from 'axios';
import ReactDOM from 'react-dom';
import {YoutubeApi, baseParams } from './YoutubeApi';

class App extends React.Component {
  constructor(props){
    super(props);
    this.state = {
        video: [], 
        videoId: '',
        selectedVideo: null}
  }

  componentDidMount(){
    this.onSubmit('llama Pajama');
  }

   onSubmit = async (searchTerm) => {
        let response = await axios.get(`https://www.googleapis.com/youtube/v3/search?q=${searchTerm}&type=video&key=AIzaSyC_0I7RZto-QzJCISRnYOJOM938SvMPmnU&part=snippet`)
        console.log('videos', response.data.items)
        this.setState({
          videoId: response.data.items[0].id.videoId,
          videos: response.data.items,  
          selectedVideo: response.data.items[0],
        }
        )};


  onVideoSelect = (video) => {
    this.setState({
      selectedVideo: video
    });
}

render(){
    return(
      <div className="ui container">
       <SearchBar onFormSubmit={this.onSubmit}/>
         <div className="ui two column stackable grid">
             <div className="ten wide column">
               <DisplayVideo video={this.state.selectedVideo} />
             </div>
             <div className="six wide column">
               <VideoCollection
                 onVideoSelect={this.onVideoSelect}
                 videos={this.state.video}
               />
           </div>
          </div>
         </div>
    );
  }
}

export default App;