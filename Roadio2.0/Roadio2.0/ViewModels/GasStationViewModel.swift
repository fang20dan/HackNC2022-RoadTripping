//
//  GasStationViewModel.swift
//  Roadio2.0
//
//  Created by will astilla on 11/6/22.
//

import Foundation
/*
class GasStationViewModel: ObservableObject{
    @Published var GasStationData: GasStationData?
    
    func getGasStations<(lat: String, lng: String) async {
        guard let url = URL(string: "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=gas&inputtype=textquery&locationbias=point:\(lat), \(lng)&fields=formatted_address%2Cname%2Cgeometry&key=AIzaSyAZ4JRLT7zandwa_yDpVq71vQZRD_n5z7U") else {
            print("Error")
            return
        }

        do {
            let (data, _) = try await URLSession.shared.data(from: url)

            if let decodedData = try? JSONDecoder().decode(GasStationData.self, from: data) {
                self.GasStationData = decodedData
            } else {
                print("Decoding error")
            }
        } catch {
            print("Error Loading Data")
        }
    }
}*/
