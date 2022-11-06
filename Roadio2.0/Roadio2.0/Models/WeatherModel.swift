// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse the JSON, add this file to your project and do:
//
//   let weatherData = try? newJSONDecoder().decode(WeatherData.self, from: jsonData)

import Foundation

// MARK: - WeatherData
struct WeatherData: Codable {
    let latitude, longitude: Int?
    let generationtimeMS: Double?
    let utcOffsetSeconds: Int?
    let timezone, timezoneAbbreviation: String?
    let elevation: Int?
    let hourlyUnits: HourlyUnits?
    let hourly: Hourly?

    enum CodingKeys: String, CodingKey {
        case latitude, longitude
        case generationtimeMS
        case utcOffsetSeconds
        case timezone
        case timezoneAbbreviation
        case elevation
        case hourlyUnits
        case hourly
    }
}

// MARK: - Hourly
struct Hourly: Codable {
    let time: [String]?
    let temperature2M, precipitation: [Double]?

    enum CodingKeys: String, CodingKey {
        case time
        case temperature2M
        case precipitation
    }
}

// MARK: - HourlyUnits
struct HourlyUnits: Codable {
    let time, temperature2M, precipitation: String?

    enum CodingKeys: String, CodingKey {
        case time
        case temperature2M
        case precipitation
    }
}

