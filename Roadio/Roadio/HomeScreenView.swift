//
//  HomeScreenView.swift
//  Roadio
//
//  Created by will astilla on 11/5/22.
//

import Foundation

import SwiftUI

struct HomeScreenView: View {
    @State var carModel: String = ""
    @State var location: String = ""
    @State var destination: String = ""

    var body: some View {
        NavigationStack {
            VStack(alignment: .center) {
                VStack(spacing: 20) {
                    HStack {
                        Image(systemName: "circle.fill")
                            .foregroundColor(.blue)
                        TextField("Starting Point", text: $location)
                            .font(.system(.title))
                            .textFieldStyle(RoundedBorderTextFieldStyle())
                    }
                    HStack {
                        Image(systemName: "mappin.and.ellipse")
                            .foregroundColor(.red)
                        TextField("Destination", text: $destination)
                            .font(.system(.title))
                            .textFieldStyle(RoundedBorderTextFieldStyle())
                    }
                    HStack {
                        Image(systemName: "car.fill")

                        TextField("Car Model (i.e. camry)", text: $carModel)
                            .font(.system(.title))
                            .textFieldStyle(RoundedBorderTextFieldStyle())
                    }
                }
            }
            .toolbar {
                ToolbarItem(placement: .navigationBarLeading) {
                    Button(action: {
                        print("Refresh")
                    }) {
                        Label("Send", systemImage: "paperplane.fill")
                    }
                }
                ToolbarItem(placement: .principal) {
                    Text("Logo")
                }
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button(action: {
                        print("Refresh")
                    }) {
                        Label("Refresh", systemImage: "arrow.clockwise")
                    }
                }
            }
            .padding()
        }
    }
}

struct HomeScreenView_Previews: PreviewProvider {
    static var previews: some View {
        HomeScreenView()
    }
}
