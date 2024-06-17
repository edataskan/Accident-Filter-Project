document.getElementById('filterForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    const params = new URLSearchParams();
    const isVehicleTypeSelected = checkboxes.length > 0;
    
    if (isVehicleTypeSelected) {
        checkboxes.forEach(checkbox => {
            params.append(checkbox.name, checkbox.value);
        });
    }
    
    fetch(`/accidents?${params.toString()}`)
        .then(response => response.json())
        .then(data => {
            const results = document.getElementById('results');
            results.innerHTML = '';
            data.forEach(accident => {
                const li = document.createElement('li');

                // Rastgele bir saat, dakika ve saniye oluştur
                const randomHour = Math.floor(Math.random() * 24);
                const randomMinute = Math.floor(Math.random() * 60);
                const randomSecond = Math.floor(Math.random() * 60);

                // Tarihe rastgele saati ekle
                const accidentDate = new Date(accident.date);
                accidentDate.setHours(randomHour, randomMinute, randomSecond);

                let vehicleType = '';
                if (accident.vehicle_type == 9) {
                    vehicleType = 'Car';
                } 
                else if (accident.vehicle_type == 1) {
                    vehicleType = 'Pedal Cycle';
                } 
                else if (accident.vehicle_type == 2) {
                    vehicleType = 'Motorcycle 50cc and under';
                } 
                else if (accident.vehicle_type == 3) {
                    vehicleType = 'Motorcycle 125cc and under';
                } 
                else if (accident.vehicle_type == 4) {
                    vehicleType = 'Motorcycle over 125cc and up to 500cc';
                } 
                else if (accident.vehicle_type == 5) {
                    vehicleType = 'Motorcycle over 500cc ';
                } 
                else if (accident.vehicle_type == 8) {
                    vehicleType = 'Taxi/Private Hire Car';
                } 
                else if (accident.vehicle_type == 10) {
                    vehicleType = 'Minibus (8-16 passenger seat)';
                } 
                else if (accident.vehicle_type == 11) {
                    vehicleType = 'Bus or Coach 17 or more passenger';
                } 
                else if (accident.vehicle_type == 16) {
                    vehicleType = 'Ridden Horse';
                } 
                else if (accident.vehicle_type == 17) {
                    vehicleType = 'Agricultural Vehicle';
                } 
                else if (accident.vehicle_type == 18) {
                    vehicleType = 'Tram';
                } 
                else if (accident.vehicle_type == 19) {
                    vehicleType = 'Van';
                }
                else if (accident.vehicle_type == 20) {
                    vehicleType = 'Goods over 3.5t and under 7.5t';
                } 
                else if (accident.vehicle_type == 21) {
                    vehicleType = 'Goods 7.5 tonnes mgw and over';
                } 
                else {
                    vehicleType = null;
                }

                if (isVehicleTypeSelected && vehicleType) {
                    li.textContent = `Accident Index: ${accident.accident_index}, Date: ${accidentDate.toISOString()}, Vehicle Type: ${vehicleType}`;
                } else {
                    li.textContent = `Accident Index: ${accident.accident_index}, Date: ${accidentDate.toISOString()}`;
                }

                results.appendChild(li);
            });
        });
});
