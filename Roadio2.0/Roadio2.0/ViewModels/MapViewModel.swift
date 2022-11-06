//
//  MapViewModel.swift
//  Roadio2.0
//
//  Created by will astilla on 11/5/22.
//

import Foundation
import PythonKit

class mapViewModel: ObservableObject {
    func loadDistance() -> String {
        let sys = Python.import("sys")
        sys.path.append("/Users/willastilla/Personal Projects/Roadio/HackNC2022-RoadTripping/Map") // path to your Python file's directory.
        let example = Python.import("map_extract") // import your Python file.
        let totalMiles = example.get_route()["distanceTotalText"] // call your Python function.}
        return String(totalMiles) ?? "N/A"
    }
}
