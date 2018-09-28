get_all = {
    "summary": "Recupera os dados de todas as notas salvas.",
    "responses": {
        "200": {
            "description": "Lista de notas",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "receipts": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
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
                            }
                        },
                        "example": {
                            "receipts": [
                                {
                                    "id": 1,
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
                            ]
                        }
                    }
                }
            }
        }
    }
}
