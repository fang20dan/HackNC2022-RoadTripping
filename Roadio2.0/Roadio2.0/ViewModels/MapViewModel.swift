//
//  MapViewModel.swift
//  Roadio2.0
//
//  Created by will astilla on 11/5/22.
//

import Foundation

class MapViewModel: ObservableObject {
    @Published var MapData: MapDirections?

    func fetchMapData(origin: String, destination: String) async {
        let newOrigin = origin.replacingOccurrences(of: " ", with: "+")
        let newDestination = destination.replacingOccurrences(of: " ", with: "+")
        guard let url = URL(string: "https://maps.googleapis.com/maps/api/directions/json?origin=\(newOrigin)&destination=\(newDestination)&key=AIzaSyAZ4JRLT7zandwa_yDpVq71vQZRD_n5z7U") else {
            print("Error")
            return
        }
        
        

        do {
            let (data, _) = try await URLSession.shared.data(from: url)

            if let decodedData = try? JSONDecoder().decode(MapDirections.self, from: data) {
                self.MapData = decodedData
            } else {
                print("Decoding error")
            }
        } catch {
            print("Error Loading Data")
        }
    }
    
    
   
}
