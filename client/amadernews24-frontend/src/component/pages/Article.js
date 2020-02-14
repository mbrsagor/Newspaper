import React, { Component } from 'react'

export default class Article extends Component {
    render(){
        return(
            <div className="content-wrapper">
                <div className="content-header">
                    <div className="container-fluid">
                        <div className="row mb-2">
                        <div className="col-sm-6">
                            <h1 className="m-0 text-dark">Article</h1>
                        </div>
                        <div className="col-sm-6">
                            <ol className="breadcrumb float-sm-right">
                                <li className="breadcrumb-item"><a href="/">Dashboard</a></li>
                                <li className="breadcrumb-item active">Article</li>
                            </ol>
                        </div>
                        </div>
                    </div>
                </div>
                    
                

            </div>
        )
    }
}
