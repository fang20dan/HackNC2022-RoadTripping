//
//  MapView.swift
//  Roadio
//
//  Created by will astilla on 11/5/22.
//

import MapKit
import SwiftUI

struct MyMapView: View {
    @State private var region: MKCoordinateRegion = MKCoordinateRegion(
        center: CLLocationCoordinate2D(latitude: MapDefaults.latitude, longitude: MapDefaults.longitude),
        span: MKCoordinateSpan(latitudeDelta: MapDefaults.zoom, longitudeDelta: MapDefaults.zoom))
        
    private enum MapDefaults {
        static let latitude = 45.872
        static let longitude = -1.248
        static let zoom = 0.5
    }

    var body: some View {
        VStack {
            
            Map(coordinateRegion: $region,
                interactionModes: .all,
                showsUserLocation: true)
        }
    }
}
