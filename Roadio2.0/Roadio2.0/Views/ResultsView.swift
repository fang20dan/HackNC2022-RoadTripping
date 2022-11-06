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

    @Binding var origin: String
    @Binding var destination: String

    var body: some View {
        VStack {
            VStack(alignment: .leading) {
                Text("Trip Overview")
                    .bold()
                    .foregroundColor(Color("SickGreen"))

                Text(mapViewModel.MapData?.routes?[0].legs?[0].distance?.text ?? "N/A")
                    .bold()
                Text(mapViewModel.MapData?.routes?[0].legs?[0].duration?.text ?? "N/A")
                    .bold()
            }
        }
        .onAppear {
            Task {
                await mapViewModel.fetchMapData(origin: origin, destination: destination)
            }
        }

        .padding()
    }
}
