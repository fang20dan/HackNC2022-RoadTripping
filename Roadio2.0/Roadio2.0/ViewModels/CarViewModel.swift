import Foundation

class MapViewModel: ObservableObject {
    @Published var CarData: CarInformation?

    func fetchCarData(make: String, model: String, year: String) async {
        guard let url = URL(string: "https://api.api-ninjas.com/v1/cars?make=\(make)&model=\(model)&year\(year)"!)!
        var request = URLRequest(url: url)
        request.setValue("FXonr/duT4t53NEl4KetRA==sILBL3Prhi1turK4", forHTTPHeaderField: "X-Api-Key")
        let task = URLSession.shared.dataTask(with: request) {(cardata, response, error) in
            guard let cardata = cardata else { return }
        if let decodedCarData = try? JSONDecoder().decode(CarInformation.self, from: cardata) {
            self.CarData = decodedCarData
        }
        }
        task.resume()
    }
}