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

    @Binding var origin: String
    @Binding var destination: String

    var body: some View {
        VStack {
            VStack(alignment: .leading) {
                Text("Trip Overview")
                    .bold()
                    .foregroundColor(Color("SickGreen"))

                Text(String(mapViewModel.MapData?.routes?[0].legs?[0].distance?.text ?? "N/A"))
                    .bold()
                Text(String(mapViewModel.MapData?.routes?[0].legs?[0].duration?.text ?? "N/A"))
                    .bold()
            }
            .font(.system(.title2))

            VStack {
                ForEach(mapViewModel.MapData?.routes?[0].legs?[0].steps ?? []) { step in
                    Text(String(step.distance?.value ?? 69))
                }
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
