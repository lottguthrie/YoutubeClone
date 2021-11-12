import React, {Component} from "react";

class SearchBar extends Component{
    constructor(props){
        super(props)
        this.state= {

        }
    }
    handleChange =(event)=>{
        this.setState({
            [event.target.name]: event.target.value
        }, ()=>console.log(this.state[event.target.name]))
    }
    handleSubmit=(event)=>{
        event.preventDefault();
        this.props.search(this.state.searchTerm)
    }

    render(){
         return (
        <div>
            <form onSubmit={this.handleSubmit}>
            <input type="text" name='searchTerm' onChange={this.handleChange} placeholder="Search Youtube" />  
            <button type='submit'>Search Videos</button>
            </form>
        </div>
    )
    }
   
}
export default SearchBar;