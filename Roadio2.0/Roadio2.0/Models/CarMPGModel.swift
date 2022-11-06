import Foundation

// MARK: - CarInformation
struct CarInformation: Codable {
    let cityMpg: Int
    let clas: String
    let combinationMpg, cylinders: Int
    let displacement: Double
    let drive, fuelType: String
    let highwayMpg: Int
    let make, model, transmission: String
    let year: Int

    enum CodingKeys: String, CodingKey {
        case cityMpg = "city_mpg"
        case clas = "class"
        case combinationMpg = "combination_mpg"
        case cylinders, displacement, drive
        case fuelType = "fuel_type"
        case highwayMpg = "highway_mpg"
        case make, model, transmission, year
    }
}

typealias Car = [CarInformation]