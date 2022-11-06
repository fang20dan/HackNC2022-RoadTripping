//
//  HomeScreenView.swift
//  Roadio
//
//  Created by will astilla on 11/5/22.
//

import Foundation

import CoreLocationUI
import MapKit
import SwiftUI

struct HomeScreenView: View {
    @StateObject var locationManager = LocationManager()
    var body: some View {
        NavigationStack {
            ZStack {
               
                Map(coordinateRegion: $locationManager.region, showsUserLocation: true)
                   
                    .onAppear{
                        locationManager.checkIfLocationServicesIsEnabled()
                    }
                VStack(alignment: .center) {
                    Image("Roadio")
                        .resizable()
                        .scaledToFit()
                    
                    Spacer()
                    
                    NavigationLink(destination: TripDetailsView()) {
                        Text("Start My Trip")
                            .bold()
                            .foregroundColor(.white)
                            .frame(width: 200, height: 60)
                            .background(Color("SickGreen"))
                            .cornerRadius(10)
                            .font(.system(.title, design: .rounded))
                    }
                    .padding(.bottom, 50)
                }
            }
            .ignoresSafeArea()
           
        }
    }
}

struct HomeScreenView_Previews: PreviewProvider {
    static var previews: some View {
        HomeScreenView()
    }
}

