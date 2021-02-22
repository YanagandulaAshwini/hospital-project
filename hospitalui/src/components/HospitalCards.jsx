import React, { useState } from 'react';
import DoctorCards from './DoctorCards';
import './HospitalCards.css';
import axios from 'axios';
import location from './location';
import history from './history';


export default class HospitalCards extends React.Component {
    state = {  
        docList: [],
        hospitalData: [],
    };
    
   
    onSubmit=(e) => {

    history.push({
        pathname: '/doctors',
       state: {
           data:this.props.hosp_id,
      },
   });
    }
  
    render(){
       
    return (       
            <div class="card">
                     <img src="https://i.pinimg.com/474x/1e/d7/b6/1ed7b68d268434b3b130f01bbff866d4.jpg" class="card-img-top" />
                    <div class="card-body container" style={{"overflow":"auto","min-width":"fit-content"}}> 
                    <h5 class="card-title" style={{"font-size":"2vw"}}>{this.props.hosp_name}</h5>
                    <p class="card-text inline-block d-block">{this.props.hosp_address}</p>
                    <p class="card-text inline-block d-block">{this.props.hosp_email}</p>
                    <p class="card-text inline-block d-block">{this.props.hosp_website}</p>
                    <p class="card-text">{this.props.hosp_mobile}</p>
                    <p class="card-text">{this.props.hosp_timings}</p>                    
                    
                    <button type="submit" onClick={this.onSubmit} value={this.props.hosp_id}  className="btn btn-success offset-0">Search</button>
                </div>
            </div>   
                    
    )
    }

}