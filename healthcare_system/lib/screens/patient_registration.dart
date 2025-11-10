import 'package:flutter/material.dart';

class NewPatientForm extends StatefulWidget {
  const NewPatientForm({super.key});

  @override
  State<NewPatientForm> createState() => _NewPatientFormState();
}

class _NewPatientFormState extends State<NewPatientForm> {
  final _formKey = GlobalKey<FormState>();

  // controllers
  final patient_name = TextEditingController();
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

  DateTime? dob;
  String? gender;

  @override
  void dispose() {
    for (final c in [
      patient_name,
      contact_number,
      address,
      emergency_contact_name,
      emergency_relationship,
      emergency_contact_number,
      height,
      weight,
      blood_pressure,
      temperature,
      heart_rate,
      allergies,
      symptoms,
      diagnosis,
      medical_history
    ]) {
      c.dispose();
    }
    super.dispose();
  }

  String? _req(String? v) =>
      (v == null || v.trim().isEmpty) ? 'Required' : null;

  String? _num(String? v) {
    if (v == null || v.trim().isEmpty) return 'Required';
    return double.tryParse(v) == null ? 'Numbers only' : null;
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(22, 22, 22, 12),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        boxShadow: const [
          BoxShadow(
            color: Colors.black12,
            offset: Offset(0, 2),
            blurRadius: 6,
          )
        ],
      ),
      child: Form(
        key: _formKey,
        child: ListView(
          children: [
            const Text(
              'Add New Patient',
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.w700),
            ),
            const SizedBox(height: 18),
            Wrap(
              spacing: 18,
              runSpacing: 14,
              children: [
                _field(
                  'Full Name',
                  _roundedField(controller: patient_name, validator: _req),
                ),
                _field(
                  'Gender',
                  DropdownButtonFormField<String>(
                    value: gender,
                    decoration: _roundedDecoration(),
                    items: const [
                      DropdownMenuItem(value: 'Male', child: Text('Male')),
                      DropdownMenuItem(value: 'Female', child: Text('Female')),
                    ],
                    onChanged: (v) => setState(() => gender = v),
                    validator: (v) => v == null ? 'Required' : null,
                  ),
                ),
                _field(
                  'Date of birth',
                  _DatePick(
                    date: dob,
                    onPick: (d) => setState(() => dob = d),
                    validator: (d) => d == null ? 'Required' : null,
                  ),
                  width: 320,
                ),
                _field(
                  'Phone Number',
                  _roundedField(
                    controller: contact_number,
                    validator: (v) {
                      if (v == null || v.isEmpty) return 'Required';
                      if (v.length < 10) return 'Enter at least 10 digits';
                      return null;
                    },
                  ),
                ),
                _field('Address',
                    _roundedField(controller: address, validator: _req)),
                _field(
                  'Emergency Contact',
                  _roundedField(controller: emergency_contact_name, validator: _req),
                ),
                _field(
                  'Relationship',
                  _roundedField(controller: emergency_relationship, validator: _req),
                ),
                _field(
                  'Phone Number',
                  _roundedField(controller: emergency_contact_number, validator: _req),
                ),
                _field(
                  'Height (cm)',
                  _roundedField(controller: height, validator: _num),
                ),
                _field(
                  'Weight (kg)',
                  _roundedField(controller: weight, validator: _num),
                ),
                _field(
                  'Blood Pressure',
                  _roundedField(controller: blood_pressure, validator: _req),
                ),
                _field(
                  'Temperature',
                  _roundedField(controller: temperature, validator: _req),
                ),
                _field(
                  'Heart Rate',
                  _roundedField(controller: heart_rate, validator: _req),
                ),
                _field(
                  'Allergies',
                  _roundedField(controller: allergies, maxLines: 2),
                ),
                _field(
                  'Symptoms',
                  _roundedField(controller: symptoms, maxLines: 2),
                ),
                _field(
                  'Diagnosis',
                  _roundedField(controller: diagnosis, maxLines: 2),
                ),
                _field(
                  'Medical History',
                  _roundedField(controller: medical_history, maxLines: 2),
                ),
              ],
            ),

            const SizedBox(height: 16),

            Align(
              alignment: Alignment.centerRight,
              child: FilledButton(
                style: FilledButton.styleFrom(
                  backgroundColor: const Color(0xFF34933B),
                  padding: const EdgeInsets.symmetric(horizontal: 28, vertical: 14),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(8),
                    ),
                    ),
                    onPressed: () {
                      if (_formKey.currentState!.validate()) {
                        ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(content: Text('Patient added')),
                          );
                          _formKey.currentState!.reset();
                          setState(() { dob = null; gender = null; });
                          }
                        },
                        child: const Text('Add',
                        style: TextStyle(color: Colors.white, fontSize: 16, fontWeight: FontWeight.w600),
                        ),
                      )
            )
          ],
        ),
      ),
    );
  }


  Widget _roundedField({
    required TextEditingController controller,
    FormFieldValidator<String>? validator,
    int maxLines = 1,
  }) {
    return TextFormField(
      controller: controller,
      maxLines: maxLines,
      validator: validator,
      decoration: _roundedDecoration(),
    );
  }

  InputDecoration _roundedDecoration() {
    return InputDecoration(
      filled: true,
      fillColor: Colors.white,
      contentPadding:
          const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(10),
        borderSide: const BorderSide(color: Color(0xFFE0E0E0), width: 1),
      ),
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(10),
        borderSide: const BorderSide(color: Color(0xFFE0E0E0), width: 1),
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(10),
        borderSide: const BorderSide(color: Color(0xFF4CAF50), width: 1.8),
      ),
    );
  }

  Widget _field(String label, Widget input, {double width = 320}) {
    return SizedBox(
      width: width,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(label, style: TextStyle(color: Colors.grey[700])),
          const SizedBox(height: 6),
          input,
        ],
      ),
    );
  }
}

class _DatePick extends FormField<DateTime?> {
  _DatePick({
    DateTime? date,
    required FormFieldSetter<DateTime?>? onPick,
    FormFieldValidator<DateTime?>? validator,
    Key? key,
  }) : super(
          key: key,
          validator: validator,
          initialValue: date,
          builder: (state) {
            final text = state.value == null
                ? ''
                : '${state.value!.year}-${state.value!.month.toString().padLeft(2, '0')}-${state.value!.day.toString().padLeft(2, '0')}';

            return InkWell(
              onTap: () async {
                final now = DateTime.now();
                final picked = await showDatePicker(
                  context: state.context,
                  firstDate: DateTime(1900),
                  lastDate: DateTime(now.year + 1),
                  initialDate: state.value ??
                      DateTime(now.year - 20, now.month, now.day),
                );
                if (picked != null) {
                  state.didChange(picked);
                  onPick?.call(picked);
                }
              },
              child: InputDecorator(
                decoration: InputDecoration(
                  filled: true,
                  fillColor: Colors.white,
                  contentPadding: const EdgeInsets.symmetric(
                      horizontal: 14, vertical: 12),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(10),
                  ),
                  enabledBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(10),
                    borderSide:
                        const BorderSide(color: Color(0xFFE0E0E0), width: 1),
                  ),
                ),
                child: Text(
                  text.isEmpty ? 'Select date' : text,
                  style: const TextStyle(fontSize: 14),
                ),
              ),
            );
          },
        );
}
