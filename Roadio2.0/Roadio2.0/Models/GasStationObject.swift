//
//  GasStationObject.swift
//  Roadio2.0
//
//  Created by will astilla on 11/6/22.
//

import Foundation


struct GasStation: Identifiable {
    var id: UUID = UUID()
    
    var name: String
    var price: String
    
    
    func calculateTotal(l: [GasStation], mpg: Int) -> Int{
        var total = 0
        for station in l{
            total += Int(station.price) ?? 0
        }
        return total
    }
    
}
