//
//  ResultsView.swift
//  Roadio
//
//  Created by will astilla on 11/5/22.
//

import Foundation
import SwiftUI

struct ResultsView: View {
    @StateObject var mapViewModel = MapViewModel()

    @State var steps: [Step] = []
    @State var tripCost: Double = 0.0

    @Binding var origin: String
    @Binding var destination: String
    @Binding var carMpg: String
    @Binding var carTankSize: String
    @Binding var carYear: String

    let weather: [Weather] = [Weather(symbol: "cloud", description: "Overcast", city: "Chapel Hill", temp: "74 F"), Weather(symbol: "sun.min", description: "Clear", city: "Chesnee", temp: "73 F"), Weather(symbol: "cloud.sun", description: "Partially Cloudy", city: "Athens", temp: "77 F"), Weather(symbol: "sun.min", description: "Clear", city: "Tuscaloosa", temp: "82 F"), Weather(symbol: "cloud.sun", description: "Partially Cloudy", city: "Jackson", temp: "81 F"), Weather(symbol: "sun.min", description: "Clear", city: "Shreveport", temp: "81 F"), Weather(symbol: "sun.min", description: "Clear", city: "Fort Worth", temp: "80 F"), Weather(symbol: "sun.min", description: "Clear", city: "Abilene", temp: "76 F"), Weather(symbol: "sun.min", description: "Clear", city: "Midland", temp: "73 F"), Weather(symbol: "sun.min", description: "Clear", city: "Van Horn", temp: "78 F"), Weather(symbol: "sun.min", description: "Clear", city: "Deming", temp: "69 F"), Weather(symbol: "sun.min", description: "Clear", city: "Tuscon", temp: "65 F"), Weather(symbol: "sun.min", description: "Clear", city: "Gila Bend", temp: "67 F"), Weather(symbol: "cloud.sun", description: "Partially Cloudy", city: "Tacna", temp: "70 F"), Weather(symbol: "sun.min", description: "Clear", city: "El Centro", temp: "73 F"), Weather(symbol: "sun.min", description: "Clear", city: "Boulevard", temp: "76 F"), Weather(symbol: "cloud.sun", description: "Clear", city: "Pine Valley", temp: "79 F"), Weather(symbol: "sun.min", description: "Clear", city: "Alpine", temp: "81 F"), Weather(symbol: "sun.min", description: "Clear", city: "Spring Valley", temp: "81 F"), Weather(symbol: "sun.min", description: "Clear", city: "San Diego", temp: "79 F")]

    let gasStations: [GasStation] = [GasStation(name: "Shell", price: "3.36"), GasStation(name: "BP", price: "3.41"), GasStation(name: "Chevron", price: "3.29"), GasStation(name: "Shell", price: "3.48"), GasStation(name: "Shell", price: "3.53"), GasStation(name: "Exxon Mobil", price: "3.93")]

    var body: some View {
        ScrollView {
            VStack(alignment: .leading) {
                HStack {
                    Image(systemName: "map")
                    Text("Trip Overview")
                }
                .bold()
                .foregroundColor(Color("SickGreen"))

                Text(String(mapViewModel.MapData?.routes?[0].legs?[0].distance?.text ?? "N/A"))

                Text(String(mapViewModel.MapData?.routes?[0].legs?[0].duration?.text ?? "N/A"))

                Divider()
                    .frame(height: 1)
                    .padding([.horizontal, .bottom], 30)

                HStack {
                    Image(systemName: "cloud")
                    Text("Trip Weather")
                }
                .bold()
                .foregroundColor(Color("SickGreen"))
                ScrollView(.horizontal) {
                    HStack {
                        ForEach(weather) { weather in

                            VStack {
                                Text(weather.city)
                                Image(systemName: weather.symbol)
                                    .bold()
                                    .font(.system(.largeTitle))
                                Text(weather.description)
                                Text(weather.temp)
                                    .bold()
                                    .font(.system(.largeTitle))
                            }
                            .frame(width: 150, height: 200)
                            .padding()
                            .background(Color("SickGreen"))
                            .foregroundColor(.white)
                            .cornerRadius(15)
                        }
                    }
                }
                .padding(.bottom, 30)

                HStack {
                    Image(systemName: "fuelpump")
                    Text("Fuel Stops")
                }
                .bold()
                .foregroundColor(Color("SickGreen"))

                ScrollView(.horizontal) {
                    HStack {
                        ForEach(gasStations) { gasStation in

                            VStack(spacing: 20) {
                                Text(gasStation.name)

                                Image(systemName: "fuelpump.circle")
                                    .bold()
                                    .font(.system(.largeTitle))
                                Text(gasStation.price)
                            }
                            .frame(width: 100, height: 200)
                            .padding()
                            .background(Color("SickGreen"))
                            .foregroundColor(.white)
                            .cornerRadius(15)
                        }
                    }
                }

                HStack {
                    Text("Estimated Trip Cost")
                        .bold()
                        .foregroundColor(Color("SickGreen"))
                }

                Text("$\(String(format: "%.2f", tripCost))")
            }
            .onAppear {
                for station in gasStations {
                    tripCost += (Double(station.price) ?? 1) * (Double(carTankSize) ?? 1)
                }
            }
        }

        .font(.system(.title2, design: .rounded))
        .onAppear {
            Task {
                await mapViewModel.fetchMapData(origin: origin, destination: destination)
            }
        }
        .toolbar {
            ToolbarItem(placement: .principal) {
                Image("Roadio")
                    .resizable()
                    .scaledToFill()
                    .padding(.top, 80)
            }
            ToolbarItem(placement: .navigationBarTrailing) {
                Button(action: {
                    print("Refresh")
                }) {
                    Label("Refresh", systemImage: "gear")
                        .foregroundColor(Color("SickGreen"))
                        .bold()
                }
            }
        }
        .padding([.top, .bottom, .leading, .trailing], 20)
    }
}
