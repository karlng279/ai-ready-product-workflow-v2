---
artifact: USM
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: po-prd-to-usm
upstream: prd.md
downstream: usl.md
---

# USM: Export Customs Clearances
id: USM-001
prd_id: PRD-001
owner: Product Team
status: draft
last_updated: 2026-05-13

## User Activities

  - activity_id: ACT-001
    name: "Determine service availability"
    description: "The customer learns whether export clearance support is available for the current booking."
    steps:
      - step_id: STEP-001
        name: "Evaluate booking context"
        description: "The booking is assessed against lane, customer, booking, and operations readiness."
        stories: [ST-001]
      - step_id: STEP-002
        name: "Present availability outcome"
        description: "The customer receives either an available service option or a clear unavailable state."
        stories: [ST-002]

  - activity_id: ACT-002
    name: "Understand service value"
    description: "The customer understands what ECC includes, excludes, and triggers after selection."
    steps:
      - step_id: STEP-003
        name: "Review service scope"
        description: "The customer reviews included support, excluded responsibilities, and service boundaries."
        stories: [ST-003]
      - step_id: STEP-004
        name: "Review next steps"
        description: "The customer understands what happens after requesting ECC."
        stories: [ST-004]

  - activity_id: ACT-003
    name: "Request clearance support"
    description: "The customer requests ECC while preserving the core booking workflow."
    steps:
      - step_id: STEP-005
        name: "Select service for booking"
        description: "The eligible customer selects or requests ECC for the booking."
        stories: [ST-005]
      - step_id: STEP-006
        name: "Complete booking decision"
        description: "The customer completes the booking whether they select ECC or continue without it."
        stories: [ST-006]

  - activity_id: ACT-004
    name: "Receive support confirmation"
    description: "The customer and operations team receive confirmation that support has been initiated."
    steps:
      - step_id: STEP-007
        name: "Confirm requested service"
        description: "The customer receives confirmation that ECC is attached or requested."
        stories: [ST-007]
      - step_id: STEP-008
        name: "Create support record"
        description: "Operations receives a support record created from booking context."
        stories: [ST-008]

  - activity_id: ACT-005
    name: "Progress support work"
    description: "Operations starts support, communicates next actions, and handles unsupported or blocked cases."
    steps:
      - step_id: STEP-009
        name: "Perform first support action"
        description: "Operations completes and records the first support action within the target window."
        stories: [ST-009]
      - step_id: STEP-010
        name: "Manage blocked support"
        description: "The customer receives clear guidance when required information is missing or support cannot proceed."
        stories: [ST-010]

  - activity_id: ACT-006
    name: "Measure service outcome"
    description: "The team measures service quality, customer feedback, and operational guardrails."
    steps:
      - step_id: STEP-011
        name: "Collect customer feedback"
        description: "The customer provides satisfaction and scope clarity feedback after support."
        stories: [ST-011]
      - step_id: STEP-012
        name: "Track service performance"
        description: "Product and operations teams track adoption, SLA, booking conversion, and service outcomes."
        stories: [ST-012]

## Notes

  - The USM avoids release slicing; Alpha/Beta/GA scope is handled through prioritization and launch constraints in downstream artifacts.
  - The first release must not imply guaranteed customs clearance or all-lane support.
