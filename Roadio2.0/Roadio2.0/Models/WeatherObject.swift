//
//  WeatherObject.swift
//  Roadio2.0
//
//  Created by will astilla on 11/6/22.
//

import Foundation

struct Weather: Identifiable {
    var id: UUID = UUID()

    var symbol: String
    var description: String
    var city: String
    var temp: String 
}
