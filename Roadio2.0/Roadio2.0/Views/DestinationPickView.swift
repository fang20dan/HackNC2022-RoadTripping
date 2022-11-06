//
//  DestinationPickView.swift
//  Roadio
//
//  Created by will astilla on 11/5/22.
//

import Foundation
import SwiftUI

struct DestinationPickView: View {
    @Binding var location: String
    @Binding var destination: String
    var body: some View {
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

       
    }
}
