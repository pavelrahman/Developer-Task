import React from 'react'
import Select from 'react-select';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import CardCar from './cardCar';


let CarCard = (props)=>{
    console.log(props.car);
        return <div className='col-md-4'>
            <div className="card" style={{width: '18rem', marginTop: '40px'}}>
                <img className="card-img-top" src={props.car.car_image} alt="Card image cap"/>
                <div className="card-body">
                    <h5 className="card-title">{props.car.tagline}</h5>
                    <p className="card-text">Manufacturer: {props.car.manufacturer}</p>
                    <p className="card-text">Model: {props.car.model}</p>
                    <p className="card-text">Mileage: {props.car.mileage}</p>
                    <p className="card-text">Transmission: {props.car.transmission}</p>
                    <button className="btn btn-primary" onClick={props.edit}>Edit</button>
                    <a href='/carlist' className="btn btn-primary" onClick={props.delete} style={{marginLeft:'10px'}}>Delete</a>
                </div>
            </div>
        </div>
}

class CreateCarList extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            carList:[]
        }

        this.deleteModel = this.deleteModel.bind(this);
        this.editModel = this.editModel.bind(this);
    }

    editModel(id){
        this.props.history.push({
            pathname: '/createcar',
            search: '?id=' + id,
        });
    }

    deleteModel(id){
        fetch("http://127.0.0.1:8000/car/api/v1/cars/"+id+"/", {
            method: 'DELETE',
            })
            .then(res => res.json())
            .then(response => {this.setState({})})
            .catch(error => console.error('Error:', error));
    }

    componentDidMount(){
        fetch("http://127.0.0.1:8000/car/api/v1/cars/", {
            method: 'GET',
        })
        .then(res => res.json())
        .then(response => {
            console.log(response);
            
            this.setState({
                carList:response
            });
        })
        .catch(error => console.error('Error:', error));
    }

    render(){
        let show = this.state.carList.map((car, index)=>{
            return <CarCard car={car} key={index} delete={this.deleteModel.bind(this, car.id)} edit={this.editModel.bind(this, car.id)}/>
        })
        return <div className='container' style={{margin:'10px'}}>
            <h1>Cars</h1>
            <div className='row'>
                {show}
            </div>
        </div>
    }
}

export default CreateCarList;