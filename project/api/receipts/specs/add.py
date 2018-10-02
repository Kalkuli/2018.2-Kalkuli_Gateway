add_specs = {
    "summary": "Salva os dados de uma nota no sistema",
    "requestBody": {
        "description": "Nota a se salvar",
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "required": ["receipt"],
                    "properties": {
                        "receipt": {
                            "type": "object",
                            "required": [
                                "company_id",
                                "emission_date",
                                "emission_place",
                                "total_price",
                                "tax_value",
                                "products"
                            ],
                            "properties": {
                                "company_id": {
                                    "type": "integer"
                                },
                                "emission_date": {
                                    "type": "string",
                                    "format": "date"
                                },
                                "emission_place": {
                                    "type": "string"
                                },
                                "total_price": {
                                    "type": "number"
                                },
                                "tax_value": {
                                    "type": "number"
                                },
                                "products": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "name": {
                                                "type": "string"
                                            },
                                            "quantity": {
                                                "type": "number"
                                            },
                                            "unit_price": {
                                                "type": "number"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "example": {
                        "receipt": {
                            "company_id": 1,
                            "emission_date": "2018-09-28",
                            "emission_place": "Shoppipsum",
                            "total_price": 10.0,
                            "tax_value": 2.0,
                            "products": [
                                {
                                    "name": "Lorem",
                                    "quantity": 2,
                                    "unit_price": 4.0
                                },
                                {
                                    "name": "Ipsum",
                                    "quantity": 1,
                                    "unit_price": 2.0
                                }
                            ]
                        }
                    }
                },
            }
        }
    },
    "responses": {
        "200": {
            "description": "object"
        }
    }
}
