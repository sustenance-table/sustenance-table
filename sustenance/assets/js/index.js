import React from 'react';
import ReactDOM from 'react-dom';
import { ListGroup, Panel, ListGroupItem, PanelGroup, Grid, Row, Col } from 'react-bootstrap';

import 'bootstrap/dist/css/bootstrap.css';


class Content extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            results: []
        };
        this.resultCallback = this.resultCallback.bind(this)
    }

    resultCallback(data) {
        this.setState({
            results: data
        });
    }

    render() {
        return (
            <div>
                <Col xs={9} md={8}>
                    <ResultDisplay results={this.state.results}/>
                </Col>
                <Col xs={3} md={4}>
                <PanelGroup accordion id="accordion-menu">
                    <CategoryList callback={this.resultCallback} url='/api/category' heading='Food Category' id='1' keyword='category'/>
                    <CategoryList callback={this.resultCallback} url='/api/nutrient' heading='Rich In' id='2' keyword='nutrient'/>
                    <CategoryList callback={this.resultCallback} url='/api/benefit' heading='Good For' id='3' keyword='benefit'/>
                </PanelGroup>
                </Col>
            </div>
        )
    }
}

class ResultDisplay extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
        <ListGroup>
            {this.props.results.map(item =>
                <ResultItem id={item.id} name={item.name} key={item.id}/>
            )}
            </ListGroup>

        )
    }
}



class ResultItem extends React.Component {
    constructor(props) {
        super(props);
        this._onClick = this._onClick.bind(this)
    }

    render() {
        return (
            <ListGroupItem onClick={this._onClick}>{this.props.name}</ListGroupItem>
        )
    }

    _onClick() {
        console.log('in on click');
    }
}

class CategoryList extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            items: [],
            results: [],
        };
        this.myCallback = this.myCallback.bind(this)

    }

    loadCategories() {
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                var parsed_data = JSON.parse(data);
                this.setState({
                    items: parsed_data
                });
            }.bind(this)
        })
    }

    componentDidMount() {
        this.loadCategories();
    }

    myCallback(dataFromChild) {
        this.props.callback(dataFromChild);
    }

    render() {
        return (
            <Panel id={"panel-"+this.props.id} eventKey={"event-"+this.props.id}>
                <Panel.Heading>
                    <Panel.Title toggle>{this.props.heading}</Panel.Title>
                </Panel.Heading>
                <Panel.Body collapsible>
                    <ListGroup>
                        {this.state.items.map(category =>
                            <ListItem callbackFromParent={this.myCallback} id={category.id} name={category.name} key={this.props.keyword+'-'+category.id} keyword={this.props.keyword}/>
                        )}
                    </ListGroup>
                </Panel.Body>
            </Panel>
        )
    }


}

class ListItem extends React.Component {
    constructor(props) {
        super(props);
        this._onClick = this._onClick.bind(this)
    }

    render() {
        return (
            <ListGroupItem onClick={this._onClick}>{this.props.name}</ListGroupItem>
        )
    }

    passBack(parsed_data) {
        this.props.callbackFromParent(parsed_data);
    }

    _onClick() {
        $.ajax({
            url: '/api/'+this.props.keyword+'/'+this.props.id+'/items',
            datatype: 'json',
            cache: false,
            success: function(data) {
                var parsed_data = JSON.parse(data);
                this.passBack(parsed_data);
            }.bind(this)

        });
    }
}


function App() {
            return (
                <Grid>
                <Row>
                    <Content />
                </Row>
                </Grid>
            )
        }


ReactDOM.render(
    <App />,
    document.getElementById('container'));