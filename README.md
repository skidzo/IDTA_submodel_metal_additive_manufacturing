# IDTA_submodel_metal_additive_manufacturing
IDTA Submodel "Metal 3D Printing Machine"


# Agenda: KickOff Meeting - IDTA Submodel "Metal 3D Printing Machine" Working Group
### (1.5 hours - 13:00 to 14:30)

1. **Welcome and Introductions** *(5 mins)*
    - Brief overview of the meeting's purpose.
    - Introduction of attendees and their roles.

2. **Project Overview and Goals** *(10 mins)*
    - Explanation of the IDTA Submodel project's objectives and significance.
    - Clarification of the focus: Creating a submodel template for Laser Powder Bed Fusion for metal powders.

3. **Scope and Boundaries** *(15 mins)*
    - Clarification of the specific scope: Laser Powder Bed Fusion as the target production method.
    - Mention of the general submodel template concept and potential inheritance from other projects.
    - Connection to the AddiBase project and potential integration with OPC UA semantics.

4. **Work Breakdown Structure (WBS)** *(15 mins)*
    - Presentation of the high-level breakdown of tasks and phases in the project.
    - Discussion on the key milestones and deliverables.

5. **Technical Details and Requirements** *(15 mins)*
    - Overview of the technical aspects: What the IDTA Submodel template should encompass.
    - Discussion on capturing essential parameters, interoperability standards, and potential OPC UA semantics.

6. **Team Roles and Responsibilities** *(10 mins)*
    - Presentation of the core team members and their roles.
    - Discussion on potential collaboration with experts outside the working group.

7. **Timeline and Milestones** *(10 mins)*
    - Presentation of the project timeline and milestones, starting from the Kickoff on September 7th, 2023.
    - Avoiding meetings around holidays to ensure consistent progress.

8. **Communication and Meetings** *(10 mins)*
    - Discussion on communication channels (email, collaboration platforms, etc.).
    - Establishment of a regular meeting schedule (frequency, time).

9. **Open Discussion and Questions** *(10 mins)*
    - Opportunity for attendees to raise questions, concerns, or suggestions.

10. **Next Steps and Adjournment** *(5 mins)*
    - Recap of the meeting's key points and action items.
    - Confirmation of the next meeting date and time.
    - Meeting adjournment.

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title IDTA Submodel Project Milestones
    section Initiation
    Kickoff Meeting     :done, 2023-08-01, 2023-08-01
    section Data Collection
    Gather Parameters   : 2023-08-02, 2023-08-10
    Collect Data       : 2023-08-11, 2023-08-20
    section Template Design
    Submodel Framework  : 2023-08-21, 2023-09-05
    Parameters Mapping : 2023-09-06, 2023-09-15
    section Testing and Refinement
    Template Validation: 2023-09-16, 2023-09-30
    Iterative Refinement: 2023-10-01, 2023-10-15
    section Finalization
    Documentation       : 2023-10-16, 2023-10-30
    Presentation        : 2023-10-31, 2023-11-05
```

---

### Project Outline: AddiBase - Enhancing Additive Manufacturing with IDTA Submodel Template and AI-driven Cognitive Production Control

**Introduction**

Additive manufacturing using metal powders for certified parts consists of complex sub-processes with many influencing parameters. The current practice of storing data in various formats leads to inefficiencies and errors in data acquisition. The AddiBase project aims to extend the existing Manufacturing Execution System with a material and process database for the Laser Powder Bed Fusion (LPBF) process. This database will be integrated with an IDTA Submodel Template for interoperability, allowing standardized data representation and seamless communication between different LPBF machines and systems. The project will also develop user-friendly Apps and a User Interface to facilitate data acquisition, analysis, and visualization. Additionally, we will explore the integration of generative AI and object-oriented AI systems for cognitive production control and problem-solving to enhance manufacturing processes.

**Project Objectives**

- Extend the Manufacturing Execution System with a material and process database, incorporating the IDTA Submodel Template for LPBF machines.
- Develop user-friendly Apps and a customizable User Interface to enable easy data acquisition and visualization for end-users.
- Implement automatic data import from existing servers to streamline data transfer and ensure comprehensive data coverage.
- Create an online catalog with detailed production profiles and parameter information for LPBF machines, enabling manufacturers to select suitable machines for their specific requirements.
- Integrate the AddiBase system with existing production planning systems to enhance production scheduling and resource allocation.
- Explore and incorporate generative AI and object-oriented AI systems for cognitive production control, predictive maintenance, and problem-solving.
- Leverage evolving AI capabilities over the next two years to enhance production efficiency, quality, and adaptability.

**Importance and Benefits**

- **Centralized Data Repository**: The integrated material and process database streamline data storage, reducing redundancy and errors.
- **Interoperability**: The IDTA Submodel Template fosters seamless communication and data exchange between LPBF machines and different systems, improving collaboration and data flow.
- **Online Catalog**: The online catalog empowers manufacturers to make informed decisions on selecting appropriate LPBF machines, optimizing production capabilities.
- **Data-Driven Decision Making**: The Apps' data visualization and analysis capabilities enable manufacturers to identify trends, anomalies, and potential improvements, fostering data-driven decision-making.
- **Enhanced Production Planning**: Integration with existing production planning systems improves production scheduling and resource allocation, leading to increased efficiency and cost-effectiveness.
- **Cognitive Production Control**: The integration of generative AI and object-oriented AI systems enables advanced production control, predictive maintenance, and problem-solving, improving overall manufacturing performance.

**Project Timeline**

```mermaid
gantt
    title IDTA Submodel "Metal 3D Printing Machine" Project Milestones
    dateFormat  YYYY-MM-DD
    section Phase 1
    Kickoff Meeting     :done, a1, 2023-09-07, 1d
    Requirement Gathering:active, a2, 2023-09-08, 5d
    Data Model Design   :a3, 2023-09-15, 10d
    section Phase 2
    Submodel Development:a4, 2023-09-25, 20d
    Integration with AddiBase:a5, 2023-10-16, 10d
    section Phase 3
    Testing and Validation:a6, 2023-10-27, 15d
    UI Development     :a7, 2023-11-11, 10d
    section Phase 4
    AI Integration     :a8, 2023-11-22, 20d
    Documentation      :a9, 2023-12-12, 10d
    section Completion
    Final Review and Testing:a10, 2023-12-22, 10d
    Project Closure    :a11, 2023-12-31, 1d
```

**Scope of Work and Relations Plan**

```mermaid
graph LR
    A[Working Group: Metal 3D Printing Machine]
    B[Submodel Template for LPBF]
    C[Additional Production Methods: EBM, DED, Binder Jetting]
    A --> B
    A --> C
```
