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
    @State var location: String = ""
    @State var destination: String = ""
    @State var seeFood: Bool = false

    var body: some View {
        VStack(alignment: .center) {
            VStack(alignment: .leading) {
                Text("Start")
                    .bold()
                    .foregroundColor(Color("SickGreen"))

                HStack {
                    Image(systemName: "mappin.and.ellipse")
                        .foregroundColor(.black)
                    TextField("Ex. Chapel Hill", text: $location)

                        .textFieldStyle(DefaultTextFieldStyle())
                }

                Divider()
                    .frame(height: 1)
                    .padding([.horizontal, .bottom], 30)

                Text("Destination")
                    .bold()
                    .foregroundColor(Color("SickGreen"))
                HStack {
                    Image(systemName: "mappin.and.ellipse")
                        .foregroundColor(.black)
                    TextField("Ex. New York City", text: $destination)

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

                    TextField("Car Model (i.e. camry)", text: $carModel)
                        .textFieldStyle(DefaultTextFieldStyle())
                }

                Divider()
                    .frame(height: 1)
                    .padding([.horizontal, .bottom], 30)
            }
            .font(.system(.title3))
            .padding(10)

            Toggle("See Food Options", isOn: $seeFood)

            NavigationLink(destination: ResultsView()) {
                Button(action: {
                    print("login tapped")

                }) {
                    Text("See Trip Details")
                        .bold()
                }
            }
        }
        .toolbar {
            ToolbarItem(placement: .principal) {
                Text("Logo")
            }
            ToolbarItem(placement: .navigationBarTrailing) {
                Button(action: {
                    print("Refresh")
                }) {
                    Label("Refresh", systemImage: "gear")
                        .foregroundColor(.black)
                        .bold()
                }
            }
        }
        .padding()
    }
}

struct TripDetailsView_Previews: PreviewProvider {
    static var previews: some View {
        TripDetailsView()
    }
}
