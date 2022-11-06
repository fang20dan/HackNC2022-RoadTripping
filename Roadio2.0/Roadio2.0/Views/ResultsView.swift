//
//  ResultsView.swift
//  Roadio
//
//  Created by will astilla on 11/5/22.
//

import Foundation
import SwiftUI


struct ResultsView: View {
    @StateObject var mvm = mapViewModel()
    var body: some View {
        VStack {
            Text(mvm.loadDistance())
        }
        .padding()
    }
}

struct ResultsView_Previews: PreviewProvider {
    static var previews: some View {
        ResultsView()
    }
}

