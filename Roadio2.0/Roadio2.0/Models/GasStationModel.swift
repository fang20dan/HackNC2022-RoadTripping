// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse the JSON, add this file to your project and do:
//
//   let gasStationData = try? newJSONDecoder().decode(GasStationData.self, from: jsonData)

import Foundation

// MARK: - GasStationData
struct GasStationData: Codable {
    let candidates: [Candidate]?
    let status: String?
}

// MARK: - Candidate
struct Candidate: Codable {
    let formattedAddress: String?
    let geometry: Geometry?
    let name: String?

    enum CodingKeys: String, CodingKey {
        case formattedAddress
        case geometry, name
    }
}

// MARK: - Geometry
struct Geometry: Codable {
    let location: Location?
    let viewport: Viewport?
}

// MARK: - Location
struct Location: Codable {
    let lat, lng: Double?
}

// MARK: - Viewport
struct Viewport: Codable {
    let northeast, southwest: Location?
}

