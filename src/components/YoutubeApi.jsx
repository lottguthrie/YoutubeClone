import axios from "axios";


const KEY = 'AIzaSyC_0I7RZto-QzJCISRnYOJOM938SvMPmnU';

export const baseParams = {
  part: "snippet",
  maxResults: 5,
  key: KEY
};

export default axios.create({
  baseURL: "https://www.googleapis.com/youtube/v3",
});