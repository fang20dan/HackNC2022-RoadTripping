//
//  TripDetailsView.swift
//  Roadio
//
//  Created by will astilla on 11/5/22.
//

import Foundation
import SwiftUI

import SwiftUI

struct TripDetailsView: View {
    @State var carModel: String = ""
    @State var carMake: String = ""
    @State var carYear: Int = 0
    @State var location: String = ""
    @State var destination: String = ""

    @State var isNavigationLinkActive = false

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading) {
                    DestinationPickView(location: $location, destination: $destination)

                    Text("Car Make")
                        .bold()
                        .foregroundColor(Color("SickGreen"))

                    HStack {
                        Image(systemName: "car.fill")

                        TextField("Car Make (i.e. Toyota)", text: $carMake)
                            .textFieldStyle(DefaultTextFieldStyle())
                    }
                    Divider()
                        .frame(height: 1)
                        .padding([.horizontal, .bottom], 30)

                    Text("Car Model")
                        .bold()
                        .foregroundColor(Color("SickGreen"))

                    HStack {
                        Image(systemName: "car.fill")

                        TextField("Car Model (i.e. Camry)", text: $carModel)
                            .textFieldStyle(DefaultTextFieldStyle())
                    }
                    Divider()
                        .frame(height: 1)
                        .padding([.horizontal, .bottom], 30)

                    Text("Car Year")
                        .bold()
                        .foregroundColor(Color("SickGreen"))

                    Picker("Please choose a color", selection: $carYear) {
                        ForEach(1950 ... 2022, id: \.self) { number in
                            Text(String(number))
                                .foregroundColor(Color("SickGreen"))
                        }
                    }
                    .pickerStyle(.inline)

                    Divider()
                        .frame(height: 1)
                        .padding([.horizontal, .bottom], 30)
                }
                .font(.system(.title2))
                .padding(10)

                Spacer()

                if !carModel.isEmpty && !location.isEmpty && !destination.isEmpty && !(carYear == 0) && !carMake.isEmpty {
                    NavigationLink(destination: ResultsView()) {
                        Text("See Trip Details")
                            .padding()
                            .foregroundColor(.white)
                            .bold()
                            .background(Color("SickGreen"))
                            .cornerRadius(15)
                    }
                } else {
                    Text("Please Fill Out All Fields Before Proceeding")
                        .padding()
                        .foregroundColor(.white)
                        .bold()
                        .background(Color(UIColor.lightGray))
                        .cornerRadius(15)
                }
            }
        }

        .navigationTitle("Test")
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
        .padding([.top, .bottom], 20)
    }
}

struct TripDetailsView_Previews: PreviewProvider {
    static var previews: some View {
        TripDetailsView()
    }
}
