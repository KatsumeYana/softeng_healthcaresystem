import 'package:flutter/material.dart';

class AddDrugForm extends StatefulWidget {
  const AddDrugForm({super.key});

  @override
  State<AddDrugForm> createState() => _AddDrugFormState();
}

class _AddDrugFormState extends State<AddDrugForm> {
  final _formKey = GlobalKey<FormState>();

  final brand_name = TextEditingController();
  final generic_name = TextEditingController();
  final drug_strength = TextEditingController();
  final quantity = TextEditingController();
  final cost = TextEditingController();
  final supplier = TextEditingController();
  final batch_number = TextEditingController();
  final storage_requirements = TextEditingController();
  final contact_person = TextEditingController();
  final phone_number = TextEditingController();

  String? dosage_form;
  String? drug_category;
  DateTime? expiration_date;
  DateTime? shipment_date;

  @override
  void dispose() {
    for (final c in [
      brand_name,
      generic_name,
      drug_strength,
      quantity,
      cost,
      supplier,
      batch_number,
      storage_requirements,
      contact_person,
      phone_number
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

  Future<DateTime?> _pickDate(DateTime? current) async {
    final now = DateTime.now();
    return showDatePicker(
      context: context,
      firstDate: DateTime(2000),
      lastDate: DateTime(now.year + 10),
      initialDate: current ?? now,
    );
  }

  InputDecoration get _roundedFieldDecoration {
    return InputDecoration(
      filled: true,
      fillColor: Colors.white,
      contentPadding:
          const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
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
        borderSide:
            const BorderSide(color: Color(0xFF34933B), width: 1.8),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(22),
      color: const Color(0xFFF1F4F2),
      child: Center(
        child: Container(
          width: double.infinity,
          constraints: const BoxConstraints(
            maxWidth: 1100,
            minHeight: 780,
          ),
          padding: const EdgeInsets.all(22),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(12),
            boxShadow: const [
              BoxShadow(
                  color: Colors.black12,
                  blurRadius: 6,
                  offset: Offset(0, 2)),
            ],
          ),
          child: Form(
            key: _formKey,
            child: SingleChildScrollView(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    "Add New Drug",
                    style: TextStyle(
                        fontSize: 20, fontWeight: FontWeight.w700),
                  ),
                  const SizedBox(height: 22),

                  Wrap(
                    spacing: 18,
                    runSpacing: 14,
                    children: [
                      _field(
                        "Brand Name",
                        TextFormField(
                          controller: brand_name,
                          validator: _req,
                          decoration: _roundedFieldDecoration,
                        ),
                      ),

                      _field(
                        "Generic Name",
                        TextFormField(
                          controller: generic_name,
                          validator: _req,
                          decoration: _roundedFieldDecoration,
                        ),
                      ),

                      _field(
                        "Strength",
                        TextFormField(
                          controller: drug_strength,
                          validator: _req,
                          decoration: _roundedFieldDecoration,
                        ),
                      ),

                      _field(
                        "Dosage Form",
                        DropdownButtonFormField<String>(
                          value: dosage_form,
                          decoration: _roundedFieldDecoration,
                          items: const [
                            DropdownMenuItem(
                                value: "Tablet", child: Text("Tablet")),
                            DropdownMenuItem(
                                value: "Capsule", child: Text("Capsule")),
                            DropdownMenuItem(
                                value: "Syrup", child: Text("Syrup")),
                            DropdownMenuItem(
                                value: "Nebule", child: Text("Nebule")),
                          ],
                          onChanged: (v) => setState(() => dosage_form = v),
                          validator: (v) =>
                              v == null ? "Required" : null,
                        ),
                      ),

                      _field(
                        "Quantity",
                        TextFormField(
                          controller: quantity,
                          validator: _num,
                          decoration: _roundedFieldDecoration,
                        ),
                      ),

                      _field(
                        "Category",
                        DropdownButtonFormField<String>(
                          value: drug_category,
                          decoration: _roundedFieldDecoration,
                          items: const [
                            DropdownMenuItem(
                                value: "Antibiotic",
                                child: Text("Antibiotic")),
                            DropdownMenuItem(
                                value: "Analgesic",
                                child: Text("Analgesic")),
                            DropdownMenuItem(
                                value: "Antihistamine",
                                child: Text("Antihistamine")),
                            DropdownMenuItem(
                                value: "NSAID", child: Text("NSAID")),
                          ],
                          onChanged: (v) =>
                              setState(() => drug_category = v),
                          validator: (v) =>
                              v == null ? "Required" : null,
                        ),
                      ),

                      _field(
                        "Cost (per unit)",
                        TextFormField(
                          controller: cost,
                          validator: _num,
                          decoration: _roundedFieldDecoration,
                        ),
                      ),

                      _field(
                        "Supplier",
                        TextFormField(
                          controller: supplier,
                          validator: _req,
                          decoration: _roundedFieldDecoration,
                        ),
                      ),

                      _field(
                        "Batch/Lot Number",
                        TextFormField(
                          controller: batch_number,
                          validator: _req,
                          decoration: _roundedFieldDecoration,
                        ),
                      ),

                      _dateField(
                        "Expiration Date",
                        expiration_date,
                        (d) => setState(() => expiration_date = d),
                      ),

                      _field(
                        "Storage Requirements",
                        TextFormField(
                          controller: storage_requirements,
                          decoration: _roundedFieldDecoration,
                        ),
                      ),

                      _dateField(
                        "Received Date",
                        shipment_date,
                        (d) => setState(() => shipment_date = d),
                      ),

                      _field(
                        "Contact Person",
                        TextFormField(
                          controller: contact_person,
                          decoration: _roundedFieldDecoration,
                        ),
                      ),

                      _field(
                        "Phone Number",
                        TextFormField(
                          controller: phone_number,
                          decoration: _roundedFieldDecoration,
                        ),
                      ),
                    ],
                  ),

                  const SizedBox(height: 22),

                  Align(
  alignment: Alignment.centerRight,
  child: FilledButton(
    style: FilledButton.styleFrom(
      backgroundColor: const Color(0xFF34933B),
      padding: const EdgeInsets.symmetric(
        horizontal: 28,
        vertical: 14,
      ),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(8),
      ),
    ),
    onPressed: () {
      if (_formKey.currentState!.validate()) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Drug added')),
        );
        _formKey.currentState!.reset();
        setState(() {
          dosage_form = null;
          drug_category = null;
          expiration_date = null;
          shipment_date = null;
        });
      }
    },
    child: const Text(
      "Add",
      style: TextStyle(
        color: Colors.white,
        fontSize: 16,
        fontWeight: FontWeight.w600,
      ),
    ),
  ),
)
                ],
              ),
            ),
          ),
        ),
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

  Widget _dateField(
      String label, DateTime? date, ValueChanged<DateTime?> onPick,
      {double width = 320}) {
    final text = date == null
        ? ""
        : "${date.year.toString().padLeft(4, '0')}-"
            "${date.month.toString().padLeft(2, '0')}-"
            "${date.day.toString().padLeft(2, '0')}";

    return SizedBox(
      width: width,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(label, style: TextStyle(color: Colors.grey[700])),
          const SizedBox(height: 6),
          InkWell(
            onTap: () async => onPick(await _pickDate(date)),
            child: InputDecorator(
              decoration: _roundedFieldDecoration.copyWith(
                hintText: "YYYY-MM-DD",
              ),
              child: Text(text.isEmpty ? "Select date" : text),
            ),
          )
        ],
      ),
    );
  }
}
