import 'package:flutter/material.dart';

class ReturningPatientScreen extends StatefulWidget {
  const ReturningPatientScreen({super.key});

  @override
  State<ReturningPatientScreen> createState() => _ReturningPatientScreenState();
}

class _ReturningPatientScreenState extends State<ReturningPatientScreen> {
  
  // Dummy patient list 
  final List<Map<String, dynamic>> _patients = [
    {
      'id': 'PT-001',
      'patient_name': 'Maria Santos',
      'gender': 'Female',
      'dob': DateTime(1995, 5, 12),
      'contact_number': '091735668942',
      'address': 'Manila',
      'emergency_contact_name': 'Ana Santos',
      'emergency_relationship': 'Mother',
      'emergency_contact_number': '09170000000',
      'height': '160',
      'weight': '55',
      'blood_pressure': '120/80',
      'temperature': '36.8',
      'heart_rate': '78',
      'allergies': 'None',
      'symptoms': 'Headache',
      'diagnosis': 'Migraine',
      'medical_history': 'Asthma',
    },
  ];

  final _searchCtrl = TextEditingController();
  Map<String, dynamic>? _selected;

  // Controllers matching EXACTLY patient registration variables
  final patient_name = TextEditingController();
  final gender = TextEditingController();
  DateTime? dob;
  final contact_number = TextEditingController();
  final address = TextEditingController();
  final emergency_contact_name = TextEditingController();
  final emergency_relationship = TextEditingController();
  final emergency_contact_number = TextEditingController();
  final height = TextEditingController();
  final weight = TextEditingController();
  final blood_pressure = TextEditingController();
  final temperature = TextEditingController();
  final heart_rate = TextEditingController();
  final allergies = TextEditingController();
  final symptoms = TextEditingController();
  final diagnosis = TextEditingController();
  final medical_history = TextEditingController();

  @override
  void dispose() {
    _searchCtrl.dispose();
    patient_name.dispose();
    gender.dispose();
    contact_number.dispose();
    address.dispose();
    emergency_contact_name.dispose();
    emergency_relationship.dispose();
    emergency_contact_number.dispose();
    height.dispose();
    weight.dispose();
    blood_pressure.dispose();
    temperature.dispose();
    heart_rate.dispose();
    allergies.dispose();
    symptoms.dispose();
    diagnosis.dispose();
    medical_history.dispose();
    super.dispose();
  }

  String _ls(Object? v) => (v ?? '').toString().toLowerCase();

  InputDecoration _roundedFieldDeco() {
    return InputDecoration(
      filled: true,
      fillColor: Colors.white,
      contentPadding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(10),
        borderSide: const BorderSide(color: Color(0xFFE0E0E0)),
      ),
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(10),
        borderSide: const BorderSide(color: Color(0xFFE0E0E0)),
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(10),
        borderSide: const BorderSide(color: Color(0xFF34933B), width: 1.8),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final keyword = _ls(_searchCtrl.text);
    final filtered = _patients.where((p) {
      return _ls(p['id']).contains(keyword) ||
          _ls(p['patient_name']).contains(keyword);
    }).toList();

    return Container(
      padding: const EdgeInsets.all(22),
      color: const Color(0xFFF1F4F2),
      child: Center(
        child: Container(
          width: double.infinity,
          constraints: const BoxConstraints(
            maxWidth: 2000,
            minHeight: 1000,
          ),
          padding: const EdgeInsets.all(22),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(12),
            boxShadow: const [
              BoxShadow(color: Colors.black12, blurRadius: 6, offset: Offset(0, 2)),
            ],
          ),
          child: SingleChildScrollView(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text('Returning Patient',
                    style: TextStyle(fontSize: 20, fontWeight: FontWeight.w700)),
                const SizedBox(height: 20),

                // SEARCH BAR
                Row(
                  children: [
                    const Spacer(),
                    SizedBox(
                      width: 340,
                      child: TextField(
                        controller: _searchCtrl,
                        decoration: _roundedFieldDeco().copyWith(
                          hintText: "Search Patient ID or Name",
                          prefixIcon: const Icon(Icons.search),
                        ),
                        onChanged: (_) => setState(() {}),
                      ),
                    ),
                    const SizedBox(width: 10),
                    Container(
                      height: 44,
                      width: 44,
                      decoration: const BoxDecoration(
                        color: Color(0xFF34933B),
                        shape: BoxShape.circle,
                      ),
                      child: IconButton(
                        icon: const Icon(Icons.search, color: Colors.white),
                        onPressed: () => setState(() {}),
                      ),
                    )
                  ],
                ),

                const SizedBox(height: 20),

                // TABLE
                ClipRRect(
                  borderRadius: BorderRadius.circular(8),
                  child: Container(
                    width: double.infinity,
                    decoration: BoxDecoration(
                      color: Colors.white,
                      border: Border.all(color: const Color(0xFFE0E0E0)),
                    ),
                    child: DataTable(
                      headingRowColor: MaterialStatePropertyAll(Colors.grey.shade100),
                      columns: const [
                        DataColumn(label: Text("Patient ID", style: TextStyle(fontWeight: FontWeight.bold))),
                        DataColumn(label: Text("Full Name", style: TextStyle(fontWeight: FontWeight.bold))),
                        DataColumn(label: Text("Gender", style: TextStyle(fontWeight: FontWeight.bold))),
                        DataColumn(label: Text("Phone", style: TextStyle(fontWeight: FontWeight.bold))),
                        DataColumn(label: Text("Action", style: TextStyle(fontWeight: FontWeight.bold))),
                      ],
                      rows: [
                        for (final p in filtered)
                          DataRow(
                            cells: [
                              DataCell(Text(p['id'])),
                              DataCell(Text(p['patient_name'])),
                              DataCell(Text(p['gender'])),
                              DataCell(Text(p['contact_number'])),
                              DataCell(
                                InkWell(
                                  onTap: () {
                                    setState(() {
                                      _selected = p;

                                      patient_name.text = p['patient_name'];
                                      gender.text = p['gender'];
                                      dob = p['dob'];
                                      contact_number.text = p['contact_number'];
                                      address.text = p['address'];
                                      emergency_contact_name.text = p['emergency_contact_name'];
                                      emergency_relationship.text = p['emergency_relationship'];
                                      emergency_contact_number.text = p['emergency_contact_number'];
                                      height.text = p['height'];
                                      weight.text = p['weight'];
                                      blood_pressure.text = p['blood_pressure'];
                                      temperature.text = p['temperature'];
                                      heart_rate.text = p['heart_rate'];
                                      allergies.text = p['allergies'];
                                      symptoms.text = p['symptoms'];
                                      diagnosis.text = p['diagnosis'];
                                      medical_history.text = p['medical_history'];
                                    });
                                  },
                                  child: Container(
                                    padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
                                    decoration: BoxDecoration(
                                      color: const Color(0xFF34933B),
                                      borderRadius: BorderRadius.circular(6),
                                    ),
                                    child: const Text("Edit",
                                        style: TextStyle(color: Colors.white)),
                                  ),
                                ),
                              ),
                            ],
                          ),
                      ],
                    ),
                  ),
                ),

                const SizedBox(height: 30),

                if (_selected != null) _editPanel(),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _editPanel() {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(22),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: const Color(0xFFE0E0E0)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text("Editing Patient: ${_selected!['id']}",
              style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
          const SizedBox(height: 20),

          Wrap(
            spacing: 18,
            runSpacing: 18,
            children: [
              _w("Full Name", patient_name),
              _dropdown("Gender", gender),
              _dobPicker(),
              _w("Phone Number", contact_number),
              _w("Address", address),
              _w("Emergency Contact", emergency_contact_name),
              _w("Relationship", emergency_relationship),
              _w("Emergency Phone", emergency_contact_number),
              _w("Height (cm)", height),
              _w("Weight (kg)", weight),
              _w("Blood Pressure", blood_pressure),
              _w("Temperature", temperature),
              _w("Heart Rate", heart_rate),
              _w("Allergies", allergies, maxLines: 2),
              _w("Symptoms", symptoms, maxLines: 2),
              _w("Diagnosis", diagnosis, maxLines: 2),
              _w("Medical History", medical_history, maxLines: 2),
            ],
          ),

          const SizedBox(height: 25),

          Align(
            alignment: Alignment.centerRight,
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
              decoration: BoxDecoration(
                color: const Color(0xFF34933B),
                borderRadius: BorderRadius.circular(8),
              ),
              child: InkWell(
                onTap: () {
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(content: Text("Patient updated (frontend only)")),
                  );
                },
                child: const Text(
                  "Update",
                  style: TextStyle(color: Colors.white, fontWeight: FontWeight.w600),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _w(String label, TextEditingController ctrl, {int maxLines = 1}) {
    return SizedBox(
      width: 300,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(label),
          const SizedBox(height: 6),
          TextField(
            controller: ctrl,
            maxLines: maxLines,
            decoration: _roundedFieldDeco(),
          ),
        ],
      ),
    );
  }

  Widget _dropdown(String label, TextEditingController ctrl) {
    return SizedBox(
      width: 300,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(label),
          const SizedBox(height: 6),
          DropdownButtonFormField<String>(
            value: ctrl.text.isEmpty ? null : ctrl.text,
            decoration: _roundedFieldDeco(),
            items: const [
              DropdownMenuItem(value: "Male", child: Text("Male")),
              DropdownMenuItem(value: "Female", child: Text("Female")),
            ],
            onChanged: (v) {
              if (v != null) ctrl.text = v;
            },
          ),
        ],
      ),
    );
  }

  Widget _dobPicker() {
    final txt = dob == null
        ? ""
        : "${dob!.year}-${dob!.month.toString().padLeft(2, '0')}-${dob!.day.toString().padLeft(2, '0')}";

    return SizedBox(
      width: 300,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text("Date of Birth"),
          const SizedBox(height: 6),
          InkWell(
            onTap: () async {
              final now = DateTime.now();
              final picked = await showDatePicker(
                context: context,
                firstDate: DateTime(1900),
                lastDate: DateTime(now.year),
                initialDate: dob ?? DateTime(now.year - 20),
              );
              if (picked != null) {
                setState(() => dob = picked);
              }
            },
            child: InputDecorator(
              decoration: _roundedFieldDeco(),
              child: Text(txt.isEmpty ? "Select date" : txt),
            ),
          )
        ],
      ),
    );
  }
}
