import Foundation

class CarViewModel: ObservableObject {
    @Published var CarData: CarInformation?

    func fetchCarData(make: String, model: String, year: String) -> String {
        var ye = ""
        guard let url = URL(string: "https://api.api-ninjas.com/v1/cars?make=toyota&model=camry&year=2005") else {
            return "banana cleaner"
        }
        var request = URLRequest(url: url)
        request.setValue("FXonr/duT4t53NEl4KetRA==sILBL3Prhi1turK4", forHTTPHeaderField: "X-Api-Key")
        let task = URLSession.shared.dataTask(with: request) {(data, response, error) in
            guard let data = data else { return }
            ye = String(data: data, encoding: .utf8)!
        }
        task.resume()
        return ye
    }
}
