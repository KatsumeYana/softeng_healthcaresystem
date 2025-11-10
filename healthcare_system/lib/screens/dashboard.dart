import 'package:flutter/material.dart';
import 'patient_registration.dart';
import 'patient_record.dart';
import 'formulary.dart';
import 'drug_form.dart';

enum DashboardTab { newPatient, returningPatient, formulary, addDrug }

class DashboardScreen extends StatefulWidget {
  const DashboardScreen({super.key});

  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  DashboardTab tab = DashboardTab.newPatient;

  @override
  Widget build(BuildContext context) {
    final side = Container(
      width: 230,
      color: Colors.white,       
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const SizedBox(height: 16),


          const _SideItem(
            icon: Icons.people_alt_outlined,
            label: 'Patient Record',
            isHeader: true,
          ),

          _NavItem(
            selected: tab == DashboardTab.newPatient,
            label: 'New Patient',
            onTap: () => setState(() => tab = DashboardTab.newPatient),
          ),

          _NavItem(
            selected: tab == DashboardTab.returningPatient,
            label: 'Returning Patient',
            onTap: () => setState(() => tab = DashboardTab.returningPatient),
          ),

          const Divider(height: 30, thickness: .8),


          const _SideItem(
            icon: Icons.inventory_2_outlined,
            label: 'Inventory',
            isHeader: true,
          ),

          _NavItem(
            selected: tab == DashboardTab.formulary,
            label: 'Formulary',
            onTap: () => setState(() => tab = DashboardTab.formulary),
          ),

          _NavItem(
            selected: tab == DashboardTab.addDrug,
            label: 'Add Drug',
            onTap: () => setState(() => tab = DashboardTab.addDrug),
          ),

          const Spacer(),

          Padding(
            padding: const EdgeInsets.all(12.0),
            child: OutlinedButton.icon(
              icon: const Icon(Icons.logout, size: 18),
              label: const Text('Logout'),
              onPressed: () => Navigator.of(context)
                  .pushReplacementNamed('/login'),
              style: OutlinedButton.styleFrom(
                foregroundColor: Colors.black87,
                side: const BorderSide(color: Colors.black45),
                minimumSize: const Size(180, 40),
              ),
            ),
          ),
        ],
      ),
    );

    Widget body;
    switch (tab) {
      case DashboardTab.newPatient:
        body = const NewPatientForm();
        break;
      case DashboardTab.returningPatient:
        body = const ReturningPatientScreen();
        break;
      case DashboardTab.formulary:
        body = const FormularyScreen();
        break;
      case DashboardTab.addDrug:
        body = const AddDrugForm();
        break;
    }

    return Scaffold(
      appBar: AppBar(
        backgroundColor: const Color(0xFF34933B),
        foregroundColor: Colors.white,
        title: const Text('St. Blaise Medical Clinic and Pharmacy'),
        elevation: 0,
      ),

      body: Row(
        children: [
          side,  
          Expanded(
            child: Container(
              color: const Color(0xFFF1F4F2), 
              child: Padding(
                padding: const EdgeInsets.all(22.0),
                child: body,
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class _SideItem extends StatelessWidget {
  final IconData icon;
  final String label;
  final bool isHeader;

  const _SideItem({
    required this.icon,
    required this.label,
    this.isHeader = false,
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return ListTile(
      dense: true,
      leading: Icon(icon, color: Colors.black87),
      title: Text(
        label,
        style: TextStyle(
          fontSize: 15,
          fontWeight: isHeader ? FontWeight.w700 : FontWeight.w500,
          color: Colors.black87,
        ),
      ),
    );
  }
}

class _NavItem extends StatelessWidget {
  final bool selected;
  final String label;
  final VoidCallback onTap;

  const _NavItem({
    required this.selected,
    required this.label,
    required this.onTap,
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      child: ListTile(
        dense: true,
        title: Text(label),
        selected: selected,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(8),
        ),

        selectedTileColor: const Color(0xFFECECEC),

        onTap: onTap,
      ),
    );
  }
}
