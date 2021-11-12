import React from 'react';
import App from './App'

function VideoCollection(props) {

    return (
        <React.Fragment>
        <div>
        {props.videos.map((element)=> <img src = {element.snippet.thumbnails.default.url} width='120' height='90'/>)}
        </div>
        </React.Fragment>
        )}
    
            
    


export default VideoCollection;